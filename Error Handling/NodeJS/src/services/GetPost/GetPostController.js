export class GetPostController {
  constructor(PostService) {
    this.PostService = PostService;
  }

  async handle(req, res, next) {
    try{
      const post = await this.PostService.execute();
      res.status(200).json(post);
    } catch (err) {
      next(err);
    }
  }
}