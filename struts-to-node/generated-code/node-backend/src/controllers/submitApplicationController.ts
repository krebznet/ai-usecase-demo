import { Request, Response, NextFunction } from 'express';
import { SubmitapplicationModel } from '../models/submitApplicationModel';

export const get = async (req: Request, res: Response, next: NextFunction) => {
  try {
    console.log(`Getting submitApplication get`);
    
    // Fetch data logic would go here
    const result = await SubmitapplicationModel.findAll();
    
    res.json({
      success: true,
      data: result
    });
  } catch (error) {
    console.error(`Error in submitApplication get:`, error);
    next(error);
  }
};