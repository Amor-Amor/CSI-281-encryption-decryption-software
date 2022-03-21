<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="../css/style.css">
        <link href="https://cdn.quilljs.com/1.3.6/quill.snow.css" rel="stylesheet">	
    </head>
    <body>
        <?php include("sidebar.php") ?>
        <?php include("head-banner.php") ?>
        <div id="page-container">
            <div id="text-box-wrapper">
                <form id="input-box">
                    <label for="plainTextInput">Encrypting...</label>
                    <input name="plainTextInput" id="plainTextInput">
                    <div id="userInput"></div>
                    <button class="button" type="submit" name="submit" onclick="encryptSubmit()"><i class="fas fa-save"></i> Submit </button>
                </form>
            </div>
            <div id="display">
                <h1> Display </h1>
                <p id="display-result"></p>
            </div>
        </div>
        <script src="https://cdn.quilljs.com/1.3.6/quill.js"></script>
        <script type="text/javascript">
            
            var toolbarOptions = [
				['bold', 'italic', 'underline', 'strike'],        // toggled buttons

				[{ 'list': 'ordered'}, { 'list': 'bullet' }],
				[{ 'script': 'sub'}, { 'script': 'super' }],      // superscript/subscript
				[{ 'indent': '-1'}, { 'indent': '+1' }],          // outdent/indent

				[{ header: [1, 2, false] }],               		  // custom button values
				[{ 'color': [] }, { 'background': [] }],          // dropdown with defaults from theme
				[{ 'font': [] }],

				['link', 'image', 'code-block'],
				];

            var userInput = new Quill("#userInput", {  modules: {
					toolbar: toolbarOptions
				},
				placeholder: "Data to be encrypted goes here...",
				theme: "snow" 
			});

            function encryptSubmit() {
                $("#input-box").on("submit",function(){
				$("#plainTextInput").val($("#userInput .ql-editor").html());
			    })	
                document.getElementById("display-result").innerHTML = $plainTextInput;
            }
        </script>
    </body>
</html>