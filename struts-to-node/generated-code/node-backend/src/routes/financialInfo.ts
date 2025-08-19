import { Router } from 'express';
import { body } from 'express-validator';
import * as financialInfoController from '../controllers/financialInfoController';
import { validateRequest } from '../middleware/validation';

const router = Router();

router.post('/', financialInfoController.post);

export default router;