import express from 'express';
import { ApiError } from './handlers/error.handler';
import { router } from './routes';

const app = express();

app.use(router)

app.use((err, req, res, next) => {
  if(err instanceof ApiError){
    res.status(err.status).json({
      message: err.message
    });
    return
  }

  res.status(500).json({
    message: 'Something went wrong.'
  })
})

export { app }