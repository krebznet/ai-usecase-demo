import { Router } from 'express';
import { body } from 'express-validator';
import * as submitApplicationController from '../controllers/submitApplicationController';
import { validateRequest } from '../middleware/validation';

const router = Router();

router.get('/', submitApplicationController.get);

export default router;