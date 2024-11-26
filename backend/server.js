const { PUBLIC_DATA } = require("./constant");
const app = require("./src/app");

app.listen(PUBLIC_DATA.port, () => {
    console.log(`The app is listening at http://localhost:${PUBLIC_DATA.port}`);
});
