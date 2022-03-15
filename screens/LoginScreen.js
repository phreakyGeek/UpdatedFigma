
export const LoginScreen = {
  afterRender: () => {
    //console.log(document.getElementById('loginform'))
    document
    .getElementById('loginform')
    ?.addEventListener('submit',async(e)=>{
      e.preventDefault();
      const formData = new FormData(e.target);
      const formProps = Object.fromEntries(formData);
      console.log('formdata',formData)
      console.log('formProps',formProps)
      location.replace('/#/main')
    })
  },
  render: () => {
    return `
        <div class="container">
          <div class="left">
              
            <h1><span class="text">WHTS Automation</span></h1>
            <div class="wrap3">
                    <div class="extraText">You need to login before making any changes</div>
                    <div class="wrap1">
                      <form id="loginform">
                        <div class="wrap">   
                                    <input class="inp" type="text" name='username' placeholder="Username"/>
                                    <input class="inp" type="text"  name='Password' placeholder="Password"/>
                        </div>
                        <div class="forgPass">Forgot Password</div>
                        <div class="buttonWrap">
                            <button  class="loginButton"> LOGIN</button>
                        </div>
                      </form>
                    </div>
            </div>      
          </div>
        
        
          <div class="right">
              <div class="sq1"></div>
              <div class="sq2"></div>
              <div class="sq3"></div>
              <a class="anchor" >
                <div class="sq4">
                    <div class="clickable" ><h1>WHTS Automation</h1></div>
                </div>
              </a>
              <div class="powerText">POWERED BY FLYWHEELS EMBEDDED RESEARCH PVT LTD</div>
          </div>
        </div>
  `;
  },
  
};
