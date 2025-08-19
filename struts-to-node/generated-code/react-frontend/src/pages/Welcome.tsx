import React from 'react';
import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from 'yup';
import { useNavigate } from 'react-router-dom';

interface WelcomeProps {
  onSubmit?: (data: any) => void;
  errors?: Record<string, string>;
}


const validationSchema = yup.object({

});

const Welcome: React.FC<WelcomeProps> = ({ onSubmit }) => {
  const navigate = useNavigate();
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting }
  } = useForm({
    resolver: yupResolver(validationSchema)
  });

  const onSubmitForm = (data: any) => {
    if (onSubmit) {
      onSubmit(data);
    }
    // Navigate to next step or show success
    console.log('Form submitted:', data);
  };

  return (
    <div className="max-w-4xl mx-auto p-6">
      <div className="bg-white rounded-lg shadow-md">
        <div className="p-6 border-b">
          <h1 className="text-2xl font-bold text-gray-900">Welcome - Truck Lease Application</h1>
          <div className="mt-4">
            {/* Progress bar */}
          </div>
        </div>
        
        <form onSubmit={handleSubmit(onSubmitForm)} className="p-6">
          {/* Form fields */}

          
          <div className="flex justify-between mt-8">
            <button
              type="button"
              onClick={() => navigate(-1)}
              className="px-6 py-2 border border-gray-300 rounded-md text-gray-700 hover:bg-gray-50"
            >
              Back
            </button>
            <button
              type="submit"
              disabled={isSubmitting}
              className="px-6 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:opacity-50"
            >
              {isSubmitting ? 'Submitting...' : 'Continue'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Welcome;
