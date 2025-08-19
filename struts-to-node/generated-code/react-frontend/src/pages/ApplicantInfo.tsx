import React from 'react';
import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from 'yup';
import { useNavigate } from 'react-router-dom';

interface ApplicantInfoProps {
  onSubmit?: (data: any) => void;
  errors?: Record<string, string>;
}


const validationSchema = yup.object({
  firstName: yup.string().required('Firstname is required'),
  lastName: yup.string().required('Lastname is required'),
  email: yup.string().email('Invalid email').required('Email is required'),
  phone: yup.string().matches(/^[\d\s\-\(\)\+\.]+$/, 'Invalid phone number').required('Phone is required'),
  ssn: yup.string().matches(/^\d{3}-?\d{2}-?\d{4}$/, 'Invalid SSN format').required('SSN is required'),
  dateOfBirth: yup.string().required('Dateofbirth is required'),
  address: yup.string().required('Address is required'),
  city: yup.string().required('City is required'),
  zipCode: yup.string().required('Zipcode is required'),
  licenseNumber: yup.string().required('Licensenumber is required'),
  state: yup.string().required('State is required'),
  licenseState: yup.string().required('Licensestate is required'),
  hasCDL: yup.string().required('Hascdl is required'),
});

const ApplicantInfo: React.FC<ApplicantInfoProps> = ({ onSubmit }) => {
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
          <h1 className="text-2xl font-bold text-gray-900">Personal Information - Truck Lease Application</h1>
          <div className="mt-4">
            {/* Progress bar */}
          </div>
        </div>
        
        <form onSubmit={handleSubmit(onSubmitForm)} className="p-6">
          {/* Form fields */}
        <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Firstname *
            </label>
            <input
              type="text"
              {...register('firstName')}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter firstname"
            />
            {errors.firstName && <p className="text-red-500 text-sm mt-1">{errors.firstName.message}</p>}
          </div>
        <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Lastname *
            </label>
            <input
              type="text"
              {...register('lastName')}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter lastname"
            />
            {errors.lastName && <p className="text-red-500 text-sm mt-1">{errors.lastName.message}</p>}
          </div>
        <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Email *
            </label>
            <input
              type="email"
              {...register('email')}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter email"
            />
            {errors.email && <p className="text-red-500 text-sm mt-1">{errors.email.message}</p>}
          </div>
        <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Phone *
            </label>
            <input
              type="tel"
              {...register('phone')}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter phone"
            />
            {errors.phone && <p className="text-red-500 text-sm mt-1">{errors.phone.message}</p>}
          </div>
        <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Ssn *
            </label>
            <input
              type="text"
              {...register('ssn')}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter ssn"
            />
            {errors.ssn && <p className="text-red-500 text-sm mt-1">{errors.ssn.message}</p>}
          </div>
        <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Dateofbirth 
            </label>
            <input
              type="date"
              {...register('dateOfBirth')}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter dateofbirth"
            />
            {errors.dateOfBirth && <p className="text-red-500 text-sm mt-1">{errors.dateOfBirth.message}</p>}
          </div>
        <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Address 
            </label>
            <input
              type="text"
              {...register('address')}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter address"
            />
            {errors.address && <p className="text-red-500 text-sm mt-1">{errors.address.message}</p>}
          </div>
        <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              City 
            </label>
            <input
              type="text"
              {...register('city')}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter city"
            />
            {errors.city && <p className="text-red-500 text-sm mt-1">{errors.city.message}</p>}
          </div>
        <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Zipcode 
            </label>
            <input
              type="text"
              {...register('zipCode')}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter zipcode"
            />
            {errors.zipCode && <p className="text-red-500 text-sm mt-1">{errors.zipCode.message}</p>}
          </div>
        <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Licensenumber 
            </label>
            <input
              type="text"
              {...register('licenseNumber')}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter licensenumber"
            />
            {errors.licenseNumber && <p className="text-red-500 text-sm mt-1">{errors.licenseNumber.message}</p>}
          </div>
        <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              State *
            </label>
            <select
              {...register('state')}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <option value="">Select State</option>
                            <option value="CA">CA</option>
              <option value="TX">TX</option>
              <option value="FL">FL</option>
              <option value="NY">NY</option>
            </select>
            {errors.state && <p className="text-red-500 text-sm mt-1">{errors.state.message}</p>}
          </div>
        <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              License State *
            </label>
            <select
              {...register('licenseState')}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <option value="">Select License State</option>
                            <option value="CA">CA</option>
              <option value="TX">TX</option>
              <option value="FL">FL</option>
              <option value="NY">NY</option>
            </select>
            {errors.licenseState && <p className="text-red-500 text-sm mt-1">{errors.licenseState.message}</p>}
          </div>
        <div className="mb-4">
            <div className="flex items-center">
              <input
                type="checkbox"
                {...register('hasCDL')}
                className="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
              />
              <label className="ml-2 block text-sm text-gray-900">
                Hascdl
              </label>
            </div>
            {errors.hasCDL && <p className="text-red-500 text-sm mt-1">{errors.hasCDL.message}</p>}
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

export default ApplicantInfo;
