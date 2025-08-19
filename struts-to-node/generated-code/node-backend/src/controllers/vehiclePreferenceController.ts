import { Request, Response, NextFunction } from 'express';
import { VehiclepreferenceModel } from '../models/vehiclePreferenceModel';

export const post = async (req: Request, res: Response, next: NextFunction) => {
  try {
    console.log(`Processing vehiclePreference post:`, req.body);
    
    // Business logic would go here
    const result = await VehiclepreferenceModel.create(req.body);
    
    // Simulate different response scenarios based on Struts forwards
    const success = Math.random() > 0.1; // 90% success rate for demo
    
    if (success) {
      res.json({
        success: true,
        message: 'Vehiclepreference post processed successfully',
        data: result,
        nextStep: '/financial-info'
      });
    } else {
      res.status(400).json({
        success: false,
        message: 'Processing failed',
        errors: ['Validation failed or business rule violation']
      });
    }
  } catch (error) {
    console.error(`Error in vehiclePreference post:`, error);
    next(error);
  }
};