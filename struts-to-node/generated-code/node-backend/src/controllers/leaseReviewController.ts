import { Request, Response, NextFunction } from 'express';
import { LeasereviewModel } from '../models/leaseReviewModel';

export const get = async (req: Request, res: Response, next: NextFunction) => {
  try {
    console.log(`Getting leaseReview get`);
    
    // Fetch data logic would go here
    const result = await LeasereviewModel.findAll();
    
    res.json({
      success: true,
      data: result
    });
  } catch (error) {
    console.error(`Error in leaseReview get:`, error);
    next(error);
  }
};