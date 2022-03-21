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
                <form>
                    <label for="plainTextInput">Encrypting...</label>
                    <input name="plainTextInput" id="plainTextInput">
                    <div id="userInput"></div>
                    <button class="button" type="submit" name="submit" onclick="encryptSubmit()"><i class="fas fa-save"></i> Save</button>
                </form>
            </div>
            <div id="display">
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

            $("#newAnnouncement").on("submit",function(){
				$("#plainTextInput").val($("#userInput .ql-editor").html());
			})	

            function encryptSubmit() {
                document.getElementById("display-result").innerHTML = $plainTextInput;
            }
        </script>
    </body>
</html>