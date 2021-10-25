import { ApiError } from "../../handlers/error.handler"

export class GetPostUseCase {
  constructor() {
  }

  async execute() {
    if(2%2 === 0){
      throw ApiError.ReferenceNotFound('Não foi possivel encontrar esta referencia.', 404)
    }
    return 'Hello World'
  }
}