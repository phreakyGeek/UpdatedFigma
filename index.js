import { ChangePartScreen } from './screens/ChangePartScreen.js';
import { MainScreen } from './screens/MainScreen.js';

import { LoginScreen } from './screens/LoginScreen.js';
// import { NewPartScreen } from './screens/NewPartScreen.js';
import { RegisterScreen } from './screens/RegisterScreen.js';
import { Add_Edit } from './screens/Add_Edit.js';
import { setup } from './screens/setup.js';

const routes = {
  '/': LoginScreen,
  '/main': MainScreen,
  '/add-edit': Add_Edit,
  '/changepart': ChangePartScreen,
  '/register': RegisterScreen,
  '/setup': setup,
  
};
const router = () => {
  const pathname = window.location.hash.substr(1);
  const route = routes[pathname || '/'];
  let text = 'no contetnet';
  if (route) {
    text = route.render();
    // console.log(text)
    document.getElementById('app').innerHTML = text;
    route.afterRender();
  }
  else{
  document.getElementById('app').innerHTML = text;
  }
};

router();
window.addEventListener('hashchange', router);
window.addEventListener('load', router);
