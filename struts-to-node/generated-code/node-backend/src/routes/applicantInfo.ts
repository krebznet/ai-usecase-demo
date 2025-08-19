import { Router } from 'express';
import { body } from 'express-validator';
import * as applicantInfoController from '../controllers/applicantInfoController';
import { validateRequest } from '../middleware/validation';

const router = Router();

router.post('/', [
  body('firstName').notEmpty().withMessage('First name is required'),
  body('lastName').notEmpty().withMessage('Last name is required'),
  body('email').isEmail().withMessage('Valid email is required'),
  body('phone').isMobilePhone('any').withMessage('Valid phone number is required'),
  validateRequest
], applicantInfoController.post);

export default router;