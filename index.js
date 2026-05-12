cat > index.js << 'EOF'
const express = require("express");
const axios = require("axios");
const _ = require("lodash");

const app = express();

app.get("/", async (req, res) => {
  const response = await axios.get("https://example.com");
  res.send(_.capitalize("vulnerable dependency test app"));
});

app.listen(3000, () => {
  console.log("Test app running on port 3000");
});
EOF
