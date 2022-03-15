export const setup = {
  render: () => {
    return `
    <div class="addWrapper">
    <div class="back" onclick="location.replace('/#/main')">
        <a    ><img src="./svg/arrow-left.svg" ></a>
    </div>
    <div class="container1">
        <div class="head">
            <span >WHTS Automation</span>
        </div>
        <div class="statusForm">
            <div class="container2 centerText">
                <button onclick="configButton()" class="configButton">Configurations</button>
                <button onclick="settingButton()" class="settingButton">Settings</button>
            </div>
            <div id="configSettings" class="container3 centerText">
                <!-- INPUTS -->
                <form id="configForm">
                    <table class="configTable">
                        <tbody>
                            <tr>
                                <td>Setup Pass</td>
                                <td><input class="inp3" type="text" /></td>
                                <td><input class="inp3" type="text" /></td>
                            </tr>
                            <tr>
                                <td>Fail</td>
                                <td><input class="inp3" type="text" /></td>
                                <td><input class="inp3" type="text" /></td>
                            </tr>
                            <tr>
                                <td>After Pass</td>
                                <td><input class="inp3" type="text" /></td>
                                <td><input class="inp3" type="text" /></td>
                            </tr>
                            <tr>
                                <td>Pass Delay</td>
                                <td><input class="inp3" type="text" /></td>
                                <td><input class="inp3" type="text" /></td>
                            </tr>
                            <tr>
                                <td>Fail Delay</td>
                                <td><input class="inp3" type="text" /></td>
                                <td><input class="inp3" type="text" /></td>
                            </tr>
                            <tr>
                                <td>After Pass Delay</td>
                                <td><input class="inp3" type="text" /></td>
                                <td><input class="inp3" type="text" /></td>
                            </tr>
                            <tr>
                                <td>After Fail Delay</td>
                                <td><input class="inp3" type="text" /></td>
                                <td><input class="inp3" type="text" /></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td colspan="2">
                                        <button class="configSubmit" type="submit">SUBMIT</button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <!-- INPUTS -->
                    
                </form>
                <form id="settingForm" class="settingForm">
                    <table>
                        <thead>
                            <tr>
                                <td colspan="2">Setting output shift register</td>
                                <td colspan="2">Setting input shift register</td>  
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>CON_DOUT_IN</td>
                                <td><input class="inp3" type="text" /></td>
                                <td>CON_IN_OUT</td>
                                <td><input class="inp3" type="text" /></td>
                            </tr>
                            <tr>
                                <td>CON_DOUT_IN</td>
                                <td><input class="inp3" type="text" /></td>
                                <td>CON_IN_OUT</td>
                                <td><input class="inp3" type="text" /></td>
                            </tr>
                            <tr>
                                <td>CON_DOUT_IN</td>
                                <td><input class="inp3" type="text" /></td>
                                <td>CON_IN_OUT</td>
                                <td><input class="inp3" type="text" /></td>
                            </tr>
                        </tbody>
                        <thead>
                            <tr>
                                <td colspan="2">Setting board parameters</td>
                                <td colspan="2">Setting indicators shift register</td>  
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>CHIPS_ON-BOARD</td>
                                <td><input class="inp3" type="text" /></td>
                                <td>OP_IN</td>
                                <td><input class="inp3" type="text" /></td>
                            </tr>
                            <tr>
                                <td>NO_OF_BOARDS</td>
                                <td><input class="inp3" type="text" /></td>
                                <td>OP_IN_LOAD</td>
                                <td><input class="inp3" type="text" /></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td></td>
                                <td>OP_IN_LOAD</td>
                                <td><input class="inp3" type="text" /></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td colspan="2">
                                        <button class="configSubmit" type="submit">SUBMIT</button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </form>
            </div>
        </div>
    </div>
</div>
              `;
  },
  afterRender: () => {
    console.log('AboutScreen afterRender');
  },
};
