import { GetPostUseCase } from "./GetPostUseCase";
import { GetPostController } from "./GetPostController";

const getPostUseCase = new GetPostUseCase();
const getPostController = new GetPostController(getPostUseCase);

export { getPostController, getPostUseCase };