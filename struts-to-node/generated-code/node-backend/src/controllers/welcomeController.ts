import { Request, Response, NextFunction } from 'express';
import { WelcomeModel } from '../models/welcomeModel';

export const get = async (req: Request, res: Response, next: NextFunction) => {
  try {
    console.log(`Getting welcome get`);
    
    // Fetch data logic would go here
    const result = await WelcomeModel.findAll();
    
    res.json({
      success: true,
      data: result
    });
  } catch (error) {
    console.error(`Error in welcome get:`, error);
    next(error);
  }
};