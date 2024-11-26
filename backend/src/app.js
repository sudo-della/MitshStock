const express = require("express")

const app = express()
const cors = require("cors")
const morgan = require("morgan");
app.use(cors())
app.use(morgan('combined'))
app.use(express.json({limit:'10mb'}))
app.use(express.urlencoded({extended:false}))

app.use("/api/v1", require("./routes"))

app.use("*",(req,res)=>{
    throw new ApiError(404,"page not found")
})
module.exports = app