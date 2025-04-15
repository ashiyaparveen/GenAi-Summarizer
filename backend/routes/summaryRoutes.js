const express = require('express');
const router = express.Router();
const { saveSummary, getUserSummaries } = require('../controllers/summaryController');

router.post('/save', saveSummary);
router.get('/history/:userId', getUserSummaries);

module.exports = router;
