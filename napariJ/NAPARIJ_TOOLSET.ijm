var dCmds = newMenu("NAPARIJ Menu Tool",
    newArray("new", "image in new viewer", "replace image", "--------", "screenshot"));

macro "NAPARIJ Menu Tool - C556L0010C546D20C445L3090C546La0b0C556Lc0d0C656De0C556Df0L0111C445L2131C556D41C546D51C445L6191C546La1b1C556Dc1C656Ld1f1C556L0222C577D32C689L4252C556D62C445L7292C546Da2C556Db2C656Lc2f2D03C546D13C667D23C689L3353C578D63C445L7383C546L93a3C556Db3C656Lc3f3D04C556D14C578L2444C689D54C578D64C556D74C445D84C546L94a4C556Db4C656Lc4f4D05C666D15C677D25C578L3565C556D75C445D85C546L95a5C556Db5C656Lc5d5C666De5C656Df5C667D06C556D16C677D26C577L3666C667D76C445L86a6C546Lb6c6C556Dd6C656Le6f6C677D07C656D17C666D27C677D37C577L4787C667D97C666Da7C656Db7C677Dc7C666Dd7C546De7C656Df7C778D08C677D18C656D28C666D38C677D48C577L5878C578D88C689L98a8C8abDb8C9bcDc8C8abDd8C666De8C656Df8C778L0929C667D39C666D49C677D59C577L6979C578D89C689L99a9C8abDb9C9bcLc9d9C578De9C556Df9C778L0a3aC656D4aC677D5aC577D6aC677D7aC578D8aC689L9aaaC8abDbaC9bcLcadaC778DeaC556DfaC99aL0b2bC778D3bC677D4bC656D5bC578L6b7bC689L8b9bC8abLabbbC9bcLcbdbC677DebC656DfbC99aL0c3cC778D4cC656D5cC677D6cC578D7cC689L8c9cC8abLacccC99aDdcC666DecC667DfcC9bcL0d1dC8abD2dC99aL3d4dC778D5dC656D6dC578D7dC689D8dC99aD9dC8abLadbdC778DcdC666DddC656DedC667DfdC9bcL0e2eC8abD3eC99aL4e5eC778D6eC656D7eC667L8eaeC666DbeC656DceC667DdeC677DeeC667DfeC9bcL0f2fC8abD3fC99aL4f6fC778L7f8fC667L9fbfC677LcfefC667Dff"{
	cmd = getArgument();
	if (cmd=="new") {
	   print("Starting new napari...");
	   path = getDir("imagej") + "scripts/NAPARIJ/open_empty_napari.py";
	   script = File.openAsString(path);
	   eval("python", script);
	   print("...DONE.");
	} 
	if(cmd=="image in new viewer") {
	   print("Starting new napari...");
	   path = getDir("imagej") + "scripts/NAPARIJ/image_in_new_viewer.py";
	   script = File.openAsString(path);
	   eval("python", script);
	   print("...DONE.");
	}
	if(cmd=="replace image") {
	   print("Replacing image in napari...");
	   path = getDir("imagej") + "scripts/NAPARIJ/replace_image.py";
	   script = File.openAsString(path);
	   eval("python", script);
	   print("...DONE.");	
	}
	if(cmd=="screenshot") {
	   print("Taking a screenshot...");
	   path = getDir("imagej") + "scripts/NAPARIJ/make_screenshot.py";
	   script = File.openAsString(path);
	   eval("python", script);
	   print("...DONE.");	
	}
}

