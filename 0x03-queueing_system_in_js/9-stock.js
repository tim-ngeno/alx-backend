import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const client = redis.createClient();

// Handle error on redis client
client.on('error', (err) => {
  console.error('Redis error:', err);
});


// Create an array with products
const listProducts = [
  {id: 1, name: 'Suitcase 250', price: 50, stock: 4},
  {id: 2, name: 'Suitcase 450', price: 100, stock: 10},
  {id: 3, name: 'Suitcase 650', price: 350, stock: 2},
  {id: 4, name: 'Suitcase 1050', price: 550, stock: 5}
];


// Function to return the data with the value of id
function getItemById(id) {
  return listProducts.find((product) => product.id === id);
}

// In stock in Redis
const reserveStockById = (itemId, stock) => {
  client.set(itemId, stock);
};

const getCurrentReservedStockById = async (itemId) => {
  const getAsync = promisify(client.get).bind(client);
  const reservedStock = await getAsync(itemId);
  return parseInt(reservedStock) || 0;
};

app.get('/list_products', (req, res) => {
  res.json(listProducts.map((product) => ({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock
  })));
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId  = parseInt(req.params.itemId);
  const product = listProducts.find((p) => p.id === itemId);
  if (!product) {
    return res.status(400).json({ status: 'Product not found' });
  }

  const currentReservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = product.stock - currentReservedStock;

  res.json({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity: currentQuantity
  });
});


// Reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = listProducts.find((p) => p.id === itemId);
  if (!product) {
    return res.status(400).json({ status: 'Product not found' });
  }

  // Get current stock availability
  const currentReserverStock = await getCurrentReservedStockById(itemId);
  if (currentReserverStock >= product.stock) {
    return res.status(400).json({status:'Not enough stock available'});
  }

  reserveStockById(itemId, currentReserverStock + 1);
  res.json({status: 'Reservation confirmed', itemId: itemId});
});

// Create an express server to listen on 1245
app.listen(1245, () => {
  console.log(`Server started on port 1245...`);
});
