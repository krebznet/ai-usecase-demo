import React from 'react';
import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from 'yup';
import { useNavigate } from 'react-router-dom';

interface VehiclePreferenceProps {
  onSubmit?: (data: any) => void;
  errors?: Record<string, string>;
}


const validationSchema = yup.object({
  specialRequirements: yup.string().required('Specialrequirements is required'),
  preferredMake: yup.string().required('Preferredmake is required'),
  maxModelYear: yup.string().required('Maxmodelyear is required'),
  trailerLength: yup.string().required('Trailerlength is required'),
  numberOfTrailers: yup.string().required('Numberoftrailers is required'),
  intendedUse: yup.string().required('Intendeduse is required'),
  milesPerYear: yup.string().required('Milesperyear is required'),
  specialRequirements: yup.string().required('Specialrequirements is required'),
  truckType: yup.string().required('Trucktype is required'),
  truckType: yup.string().required('Trucktype is required'),
  truckType: yup.string().required('Trucktype is required'),
  trailerType: yup.string().required('Trailertype is required'),
  trailerType: yup.string().required('Trailertype is required'),
  trailerType: yup.string().required('Trailertype is required'),
  trailerType: yup.string().required('Trailertype is required'),
});

const VehiclePreference: React.FC<VehiclePreferenceProps> = ({ onSubmit }) => {
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
          <h1 className="text-2xl font-bold text-gray-900">Vehicle Preferences - Truck Lease Application</h1>
          <div className="mt-4">
            {/* Progress bar */}
          </div>
        </div>
        
        <form onSubmit={handleSubmit(onSubmitForm)} className="p-6">
          {/* Form fields */}
        <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Specialrequirements
            </label>
            <textarea
              {...register('specialRequirements')}
              rows={3}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter specialrequirements..."
            />
            {errors.specialRequirements && <p className="text-red-500 text-sm mt-1">{errors.specialRequirements.message}</p>}
          </div>
        <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Preferredmake
            </label>
            <select
              {...register('preferredMake')}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <option value="">Select Preferredmake</option>
              {/* Options populated based on field type */}
            </select>
            {errors.preferredMake && <p className="text-red-500 text-sm mt-1">{errors.preferredMake.message}</p>}
          </div>
        <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Maxmodelyear 
            </label>
            <input
              type="text"
              {...register('maxModelYear')}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter maxmodelyear"
            />
            {errors.maxModelYear && <p className="text-red-500 text-sm mt-1">{errors.maxModelYear.message}</p>}
          </div>
        <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Trailerlength 
            </label>
            <input
              type="text"
              {...register('trailerLength')}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter trailerlength"
            />
            {errors.trailerLength && <p className="text-red-500 text-sm mt-1">{errors.trailerLength.message}</p>}
          </div>
        <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Numberoftrailers 
            </label>
            <input
              type="text"
              {...register('numberOfTrailers')}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter numberoftrailers"
            />
            {errors.numberOfTrailers && <p className="text-red-500 text-sm mt-1">{errors.numberOfTrailers.message}</p>}
          </div>
        <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Intendeduse 
            </label>
            <input
              type="text"
              {...register('intendedUse')}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter intendeduse"
            />
            {errors.intendedUse && <p className="text-red-500 text-sm mt-1">{errors.intendedUse.message}</p>}
          </div>
        <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Milesperyear 
            </label>
            <input
              type="text"
              {...register('milesPerYear')}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter milesperyear"
            />
            {errors.milesPerYear && <p className="text-red-500 text-sm mt-1">{errors.milesPerYear.message}</p>}
          </div>
        <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Specialrequirements
            </label>
            <textarea
              {...register('specialRequirements')}
              rows={3}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter specialrequirements..."
            />
            {errors.specialRequirements && <p className="text-red-500 text-sm mt-1">{errors.specialRequirements.message}</p>}
          </div>
        <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Trucktype 
            </label>
            <input
              type="text"
              {...register('truckType')}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter trucktype"
            />
            {errors.truckType && <p className="text-red-500 text-sm mt-1">{errors.truckType.message}</p>}
          </div>
        <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Trucktype 
            </label>
            <input
              type="text"
              {...register('truckType')}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter trucktype"
            />
            {errors.truckType && <p className="text-red-500 text-sm mt-1">{errors.truckType.message}</p>}
          </div>
        <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Trucktype 
            </label>
            <input
              type="text"
              {...register('truckType')}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter trucktype"
            />
            {errors.truckType && <p className="text-red-500 text-sm mt-1">{errors.truckType.message}</p>}
          </div>
        <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Trailertype 
            </label>
            <input
              type="text"
              {...register('trailerType')}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter trailertype"
            />
            {errors.trailerType && <p className="text-red-500 text-sm mt-1">{errors.trailerType.message}</p>}
          </div>
        <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Trailertype 
            </label>
            <input
              type="text"
              {...register('trailerType')}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter trailertype"
            />
            {errors.trailerType && <p className="text-red-500 text-sm mt-1">{errors.trailerType.message}</p>}
          </div>
        <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Trailertype 
            </label>
            <input
              type="text"
              {...register('trailerType')}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter trailertype"
            />
            {errors.trailerType && <p className="text-red-500 text-sm mt-1">{errors.trailerType.message}</p>}
          </div>
        <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Trailertype 
            </label>
            <input
              type="text"
              {...register('trailerType')}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter trailertype"
            />
            {errors.trailerType && <p className="text-red-500 text-sm mt-1">{errors.trailerType.message}</p>}
          </div>
          
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

export default VehiclePreference;
