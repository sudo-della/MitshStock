require("dotenv").config();

const morgan = require("morgan"); // Import morgan
const { PUBLIC_DATA } = require("./constant");
const app = require("./src/app");
const { ConnectDB } = require("./src/config/db.config");

// Set up morgan with a format
app.use(morgan('combined')); // or 'dev', 'short'

// Connect to the database
ConnectDB();

// Start the server
app.listen(PUBLIC_DATA.port, () => {
    console.log(`The app is listening at http://localhost:${PUBLIC_DATA.port}`);
});
