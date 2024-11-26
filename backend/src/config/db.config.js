const { default: mongoose } = require("mongoose");
const { PUBLIC_DATA } = require("../../constant");

exports.ConnectDB = async()=>{
    try{
        await mongoose.connect(PUBLIC_DATA.mongo_url)
        console.log(`The app is connected with ${mongoose.connection.host}`);

    }catch(error){
        mongoose.disconnect();
        process.exit(1)
    }
}