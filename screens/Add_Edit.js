function onloading(){
 let  table_pinnames = document.getElementById('pinnames');
  console.log(table_pinnames);
  let s = "";
  for (let i = 0; i < 128; i++) {
    s += "<div>Pin"+String(i);
    s += " Name <input class='inp1' id='pinname "+String(i)+"'>";
    s += "Netlist<input class='inp1' id='pin "+String(i)+"'>";
    s += "</div>";
  }
  table_pinnames.innerHTML = s;
}
function load_master(dbnet,names)
{
da = JSON.parse(names);
das = JSON.parse(dbnet);
for(let i=0;i<128;i++)
{
  if(da["Pin"+String(i)]  != undefined)
  {
    document.getElementById('pinname '+String(i)).value=da["Pin"+String(i)];
  }
  if(das["pin "+String(i)]  != undefined)
  {
    document.getElementById('pin '+String(i)).value=das["pin "+String(i)];
  }
}

}
let learnt_data;
function netlist_load(data){
  learn_data = data
  // clean table data
  document.getElementById("message").innerText = "";
  for (let i = 0; i < 128; i++) {
      document.getElementById('pin '+String(i)).value="";
  }
  if (Object.keys(learn_data).length === 0)
  {
      document.getElementById("message").innerText = "Wire Harness not connected Please connect and learn again";
  }else
  {
      for (var k in data)
      {
          document.getElementById(k).value = data[k];
      }
      document.getElementById("status").innerText = "Learn Complete";
  }     

}

function save_pno()
{
let da = {};
for (let i=0;i<128;i++)
{
  if (document.getElementById('pinname '+String(i)).value != "")
  {
    da["Pin"+String(i)]=document.getElementById('pinname '+String(i)).value;
  }
}

document.getElementById("message").innerText = "";
if (document.getElementById("partNO").value == "")
{
  document.getElementById("message").innerText = "Insert a part no to save";
}
else
{
  document.getElementById("status").text = "saving ... ";
  window.pywebview.api.save_masterdata(document.getElementById("partNO").value,JSON.stringify(da));
}
}


export const Add_Edit = {
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
                <div class="status">STATUS</div>
                <div class="container2">
                    <button onclick="save_pno();" class="button1">Save Names</button>
                    <button onclick="document.getElementById('status').innerText='Learning ...';window.pywebview.api.get_netlist('title')" class="button2">Learn NetList</button>
                </div>
                <div class="container3">
                    <form>
                        <!-- INPUTS -->
                        <div>
                            Part Number 
                            <input class="inp2" id="partNO" onchange="window.pywebview.api.load_masterdata(document.getElementById('partNO').value);">
                        </div>
                            <!-- input starts here -->
                            <div id="pinnames" class="similarInput">
                                
                            </div>
                            <!-- input ends here -->    
                        <!-- INPUTS -->
                        <div>
                            <button class="submit1" type="submit">SUBMIT</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
              `;
  },
  afterRender: () => {
    setTimeout(onloading, 2000);
    console.log('AboutScreen afterRender');
  },
};
