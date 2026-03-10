import { Link } from 'react-router-dom';

const NotFoundPage = () => {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full text-center space-y-8">
        <div>
          <h1 className="text-9xl font-extrabold text-blue-600 tracking-widest">
            404
          </h1>
          <div className="bg-blue-600 px-2 text-sm rounded rotate-12 absolute -mt-10 ml-20 inline-block text-white font-semibold">
            Page Not Found
          </div>
        </div>
        
        <div className="space-y-4">
          <h2 className="text-3xl font-bold text-gray-900 sm:text-4xl">
            Lost in space?
          </h2>
          <p className="text-lg text-gray-600">
            The page you're looking for doesn't exist or has been moved to another universe.
          </p>
        </div>

        <div className="flex justify-center space-x-4">
          <Link
            to="/"
            className="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors duration-200"
          >
            Go Back Home
          </Link>
          <button 
            onClick={() => window.history.back()}
            className="inline-flex items-center px-6 py-3 border border-gray-300 text-base font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors duration-200"
          >
            Go Back
          </button>
        </div>
      </div>
    </div>
  );
};

export default NotFoundPage;
