import * as yup from 'yup';

export const applicantFormSchema = yup.object({
  firstName: yup.string().required('Firstname is required'),
  lastName: yup.string().required('Lastname is required'),
  email: yup.string().email('Invalid email').required('Email is required'),
  phone: yup.string().matches(/^[\d\s\-\(\)\+\.]+$/, 'Invalid phone number').required('Phone is required'),
  ssn: yup.string().matches(/^\d{3}-?\d{2}-?\d{4}$/, 'Invalid SSN format').required('SSN is required'),
  dateOfBirth: yup.string().required('Dateofbirth is required'),
  address: yup.string().required('Address is required'),
  city: yup.string().required('City is required'),
  state: yup.string().required('State is required'),
  zipCode: yup.string().required('Zipcode is required'),
  licenseNumber: yup.string().required('Licensenumber is required'),
  licenseState: yup.string().required('Licensestate is required'),
  hasCDL: yup.string().required('Hascdl is required'),
});
export const vehiclePreferenceFormSchema = yup.object({
  truckType: yup.string().required('Trucktype is required'),
  preferredMake: yup.string().required('Preferredmake is required'),
  maxModelYear: yup.string().required('Maxmodelyear is required'),
  trailerType: yup.string().required('Trailertype is required'),
  trailerLength: yup.string().required('Trailerlength is required'),
  numberOfTrailers: yup.string().required('Numberoftrailers is required'),
  intendedUse: yup.string().required('Intendeduse is required'),
  milesPerYear: yup.string().required('Milesperyear is required'),
  specialRequirements: yup.string().required('Specialrequirements is required'),
});
