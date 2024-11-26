class ApiError extends Error{
    statusCode = 500
    constructor(statusCode,msg){
        super(msg)
        this.message = msgthis.statusCode = statusCode;
    }
}