import { Router } from 'express';
import { body } from 'express-validator';
import * as vehiclePreferenceController from '../controllers/vehiclePreferenceController';
import { validateRequest } from '../middleware/validation';

const router = Router();

router.post('/', [
  body('truckType').notEmpty().withMessage('Truck type is required'),
  body('trailerType').notEmpty().withMessage('Trailer type is required'),
  validateRequest
], vehiclePreferenceController.post);

export default router;