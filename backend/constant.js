class PUBLIC_DATA{

    static port = process.env.PORT || 4000
    static mongo_url = process.env.MONGO_URL || 'mongodb://localhost/inventry'
    
}

module.exports = {
    PUBLIC_DATA
}