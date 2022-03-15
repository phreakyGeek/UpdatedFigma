let master_data= {};
function onloading() {
window.pywebview.api.loadme("text","");
};
function failed()
{
document.getElementById('fail').style.display = 'block';
document.getElementById('pass').style.display = 'none';
document.getElementById('nohar').style.display = 'none';
}
function passed()
{
document.getElementById('fail').style.display = 'none';
document.getElementById('pass').style.display = 'block';
document.getElementById('nohar').style.display = 'none';
}
function noharness()
{
document.getElementById('fail').style.display = 'none';
document.getElementById('pass').style.display = 'none';
document.getElementById('nohar').style.display = 'block';
}
//style="display:flex;justify-content:space-between;align-items:center;margin:0 90px"

export const MainScreen = {
    render: () => {
      return `
  
    <div class="dashHeadDiv">
        <div class="dashHead">WHTS Automation</div>
    </div>
    <div class="sidebar">
        <div class="tabs" onClick="location.replace('/')"><span>LOGIN</span></div>
        <div class="tabs" onClick="location.replace('/#/register')"><span>NEW USER</span></div>
        <div class="tabs" onclick="location.replace('/#/add-edit')"><span>ADD / EDIT PART NO</span></div>
        <div class="tabs" onclick="location.replace('/#/changepart')"><span>CHANGE PART NO</span></div>
        <div class="tabs" onclick="location.replace('/#/setup')"><span>SETUP</span></div>
    </div>
    <div class="content">
        <div class="contHead">TEST RESULT</div>
        <div class="result">
            <div class="resWrap">
                <div class="result1">PASS</div>
                <div class="result2">NO-HARNESS</div>
                <div class="result3">FAIL</div>
                </div>
            <div class="tableWrap" >
            <div class="tableText">Logged in user : <span>Flywheels</span></div>
            </div>
            <button style="margin-left:36%;" class="button1" onclick="window.pywebview.api.test_part(master_data.PartNo);">TEST</button>
            <div class="resTable">
                <table class="tableWrap1">
                    <thead class="tableHead1">
                        <tr>
                            <span><td class="colapse" colspan="8">PART NO : 9867236791</td></span>
                        </tr>
                        <tr>
                            <td rowspan="2" class="goGreen">Good parts</td>
                            <td colspan="4">Rejection</td>
                            <td rowspan="2">Total Rejection</td>
                            <td rowspan="2">Tested</td>
                            <td rowspan="2">Rejection % </td>
                        </tr>
                        <tr>
                            <td>Continuity</td>
                            <td>Orientation</td>
                            <td>Hiplot</td>
                            <td class="tableDataSpaceIR">IR</td>
                        </tr>
                    </thead>
                    <tbody class="tableBody1">
                        <tr>
                            <td class="goGreen">20</td>
                            <td>10</td>
                            <td></td>
                            <td></td>
                            <td></td>
                            <td>10</td>
                            <td>28</td>
                            <td>30%</td>
                        </tr>
                    </tbody>
                </table>
            </div>
                
        </div>
    </div>
              `;
    },
    afterRender: () => {
        //console.log('h')
        setTimeout(onloading, 2000);
        // document.onload = onloading;
    },
  };