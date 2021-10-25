export class ApiError {
  constructor(message, status = 200) {
    this.status = status;
    this.message = message;
  }
  
  static MissingData(message, status = 200) {
    return new ApiError(message, status);
  }

  static ReferenceNotFound(message, status = 200) {
    return new ApiError(message, status);
  }
}