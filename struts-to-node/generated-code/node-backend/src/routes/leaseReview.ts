import { Router } from 'express';
import { body } from 'express-validator';
import * as leaseReviewController from '../controllers/leaseReviewController';
import { validateRequest } from '../middleware/validation';

const router = Router();

router.get('/', leaseReviewController.get);

export default router;