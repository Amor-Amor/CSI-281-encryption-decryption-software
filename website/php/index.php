<?PHP

$uploadedFile = "../include/specials.php";

if($_SERVER['REQUEST_METHOD'] == "POST"))
{
	//open file and write data from text box
    $fs = fopen($uploadedFile, "w");

    fwrite($fs, $_POST['plainTextInput']);
    fclose($fs);
}

// use Markdownify\Converter; 
// require '../vendor/autoload.php';

$plainTextInput = htmlspecialchars(implode('', file($uploadedFile)));


?>

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
                    <button class="button" type="submit" name="submit" onclick="savePushed()"><i class="fas fa-save"></i> Save</button>
                </form>
            </div>
            <div class="announcements-content">
                <div id="display">
					<?php
						$plainTextInput = file_get_contents($uploadedFile);
						$regex = "/!?\[.*?\)/";  //Looks for expressions starting with "[" and ending with ")" Matches if there is a "!" in front as well to get the "!"
						$userInput = preg_replace_callback($regex, function ($matches) {
							if ($matches[0][0] == '!')  //If match starts with a "!", it is ignored because it's an image
							{
								return $matches[0];
							}

							preg_match("/\[.*?\]/", $matches[0], $textMatches);  //isolates the text piece
							preg_match("/\(.*?\)/", $matches[0], $linkMatches);  //isolates the address piece

							$text = substr($textMatches[0], 1, strlen($textMatches[0]) - 2);  //Cuts off the brackets
							$link = substr($linkMatches[0], 1, strlen($linkMatches[0]) - 2);  //Cuts of the parentheses

							$newCode = '<a href="' . $link . '" target="blank">' . $text . '</a>';  //Assembles html code

							return $newCode;
						}, $userInput);
						echo $userInput;
                    ?>
                </div>
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
        </script>
    </body>
</html>