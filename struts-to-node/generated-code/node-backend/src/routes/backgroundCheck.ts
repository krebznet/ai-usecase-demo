import { Router } from 'express';
import { body } from 'express-validator';
import * as backgroundCheckController from '../controllers/backgroundCheckController';
import { validateRequest } from '../middleware/validation';

const router = Router();

router.post('/', backgroundCheckController.post);

export default router;