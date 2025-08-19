import { Router } from 'express';
import { body } from 'express-validator';
import * as welcomeController from '../controllers/welcomeController';
import { validateRequest } from '../middleware/validation';

const router = Router();

router.get('/', welcomeController.get);

export default router;