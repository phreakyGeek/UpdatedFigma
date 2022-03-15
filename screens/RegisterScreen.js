export const RegisterScreen = {
  render: () => {
    return `
    <div class="back" onclick="location.replace('/#/main')">
        <a    ><img src="./svg/arrow-left.svg" ></a>
    </div>
    <div class="container5">
    
    <div class="usrleft">
    
      <h1><span class="usrtext">WHTS Automation</span></h1>
      
      <div class="wrap3 usrwrap3">
        <form>
          <input class="inp" type="text" name='username' placeholder="Username"/>
          <input class="inp" type="text" name='Email' placeholder="Email"/>
          <input class="inp" type="text" name='Password' placeholder="Password"/>
          <input class="inp" type="text" name='confirmPassword' placeholder="Confirm Password"/>
          <div class="partSelector">
            <select class="usrpartDrop" name="role" id="role">
              <option value="role">Role</option>
              <option value="admin">Admin</option>
              <option value="supervisor">Supervisor</option>
              <option value="technician">Technician</option>
            </select>
          </div>
          <div class="usrButton">
            <button class="newUserSubmit" type="submit">SUBMIT</button>
          </div>
      </form>
      </div>
    </div>
    
    
    
    <div class="usrright">
        <div class="usrsq1"></div>
        <div class="usrsq2"></div>
        <div class="usrsq3"></div>
        <a class="anchor" >
          <div class="usrsq4">
              <div class="clickable" ><h1>WHTS Automation</h1></div>
          </div>
        </a>
        <div class="usrpowerText">POWERED BY FLYWHEELS EMBEDDED RESEARCH PVT LTD</div>
    </div>
  </div>
              `;
  },
  afterRender: () => {
    console.log('AboutScreen afterRender');
  },
};
