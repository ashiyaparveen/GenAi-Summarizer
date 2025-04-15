// summaryHistory.js (Mongoose Schema - Node.js)
const mongoose = require('mongoose');

const SummarySchema = new mongoose.Schema({
  userId: {
    type: String,
    required: true
  },
  originalContent: {
    type: String,
    required: true
  },
  summary: {
    type: String,
    required: true
  },
  topics: [String], // extracted or user-preferred topics
  createdAt: {
    type: Date,
    default: Date.now
  }
});

module.exports = mongoose.model('SummaryHistory', SummarySchema);
