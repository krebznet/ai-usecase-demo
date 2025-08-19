import { Request, Response, NextFunction } from 'express';
import { FinancialinfoModel } from '../models/financialInfoModel';

export const post = async (req: Request, res: Response, next: NextFunction) => {
  try {
    console.log(`Processing financialInfo post:`, req.body);
    
    // Business logic would go here
    const result = await FinancialinfoModel.create(req.body);
    
    // Simulate different response scenarios based on Struts forwards
    const success = Math.random() > 0.1; // 90% success rate for demo
    
    if (success) {
      res.json({
        success: true,
        message: 'Financialinfo post processed successfully',
        data: result,
        nextStep: '/background-check'
      });
    } else {
      res.status(400).json({
        success: false,
        message: 'Processing failed',
        errors: ['Validation failed or business rule violation']
      });
    }
  } catch (error) {
    console.error(`Error in financialInfo post:`, error);
    next(error);
  }
};