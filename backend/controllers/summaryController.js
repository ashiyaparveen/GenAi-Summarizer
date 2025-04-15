const Summary = require('../models/summaryHistory');

exports.saveSummary = async (req, res) => {
  try {
    const { userId, originalContent, summary, topics } = req.body;
    const newSummary = new Summary({ userId, originalContent, summary, topics });
    await newSummary.save();
    res.status(201).json({ message: "Summary saved!" });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

exports.getUserSummaries = async (req, res) => {
  try {
    const { userId } = req.params;
    const summaries = await Summary.find({ userId }).sort({ createdAt: -1 });
    res.json(summaries);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};
