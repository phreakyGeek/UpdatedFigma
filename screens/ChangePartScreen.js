let data
function load_list()
{
  data = window.pywebview.api.get_allpnos("").then((d)=>{ 
  data =JSON.parse(d);  
  let s = "";
  for (let i=0 ; i< data.length;i++)
  {
    s += "<option value='"+data[i].PartNo+"'>"+data[i].PartNo+'</option>';
  }
  document.getElementById("PartNo").innerHTML = s; 
  });
}



export const ChangePartScreen = {
  render: () => {
    return `
    <div class="addWrapper">
    <div class="back" onclick="location.replace('/#/main')">
        <a    ><img class="filterSVG" src="./svg/arrow-left.svg" ></a>
    </div>
    <div class="container1">
        <div class="head">
            <span >WHTS Automation</span>
        </div>
        <div class="statusForm">
            <div class="container4">
                <div class="partText">You need to login before making any changes</div>
                <div class="partSelector">Select Part No
                          <select class="partDrop" name="parts" id="PartNo">
                            
                          </select>
                </div>
                <div class="loadButtonDiv">
                    <button class="loadButton" onclick="window.pywebview.api.write_curr(document.getElementById('PartNo').value)" type="button">Load Part No</button>
                </div>
                <div class="changePartSubmitDiv">
                    <button class="changePartSubmit" type="button">SUBMIT</button>
                </div>
            </div>
        </div>
    </div>
</div>
              `;
  },
  afterRender: () => {
    setTimeout(load_list, 2000);
    console.log('ContactScreen afterRender');
  },
};
