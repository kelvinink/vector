const express = require('express');
const app = express();
const path = require('path');

// Define a route to serve images based on ins_id
app.get('/inscription/:ins_id', (req, res) => {
  const insId = req.params.ins_id;
  const imagePath = path.join(__dirname, 'static', `${insId}.png`);

  res.sendFile(imagePath, (err) => {
    if (err) {
      // Handle error if the image file cannot be found or sent
      console.error(err);
      res.status(404).send('Image Not Found');
    }
  });
});

// Start the server
const port = 80;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});