require('dotenv').config(); // 👉 Add this at the top!

const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const summaryRoutes = require('./routes/summaryRoutes');

const app = express();
app.use(cors());
app.use(express.json());

// MongoDB connection
mongoose.connect(process.env.MONGO_URI)
  .then(() => console.log("MongoDB connected"))
  .catch(err => console.log(err));

// Routes
app.use('/api/summary', summaryRoutes);

// Start server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
