import { Router } from 'express';

import { getPostController } from './services/GetPost'

const router = Router();

router.use('/', async (request, response, next) => getPostController.handle(request, response, next));

export { router };