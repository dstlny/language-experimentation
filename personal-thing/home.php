<?php
    require_once 'header.php';
?>
<div style="display:flex; padding: 0; margin: 0; list-style: none; align-items: center; justify-content: center;">
    <fieldset>
        <legend>Generate Hashes for the memes</legend>
    <fieldset>
    <legend>Dialogs</legend>
         <a style="border: 1px solid black; padding: 5px;" onClick="window.alert('This program allows a user to find out whether or not file-system contents have been potentially tampered with or not.');">About</a>
         &emsp;<a style="border: 1px solid black; padding: 5px;" onClick="window.alert('One day i got bored and decided to try mirror one of my Java projects in PHP. \nJava sourcecode is in my github below\nhttps://github.com/dstlny/SSD-HashingApplication');">Idea</a><br>
    </fieldset>
    <form method="post" action="">
        <fieldset>
        <legend>Select Algorithm to use</legend>
            <select name="HashSelect">
                <?php
                 $array = hash_algos();
                 for($i = 0; $i < count($array); $i++){
                     echo '<option value="'.$array[$i].'">'.$array[$i].'</option>';
                 }
              ?>
            </select>
        </fieldset>
        <fieldset>
        <legend>Gen Hash</legend>
            <input type="text" placeholder="String..." name="txtString">
            <button type="submit" name="register" value="submit">Gen Hash</button>
            <?php
                if(empty($_POST['txtString'])){
                    echo "<p style='color: red; padding: 0; margin-top:1; margin-bottom:1;'>* This must have content</p>";
                }
            ?>
        </fieldset>
    </form>
</div>
<br>
<?php
if(!empty($_POST['txtString'])){
    $input = $_POST['txtString'];
    $selected_val = $_POST['HashSelect'];
    
    class generateHash{
        
        function selectAlgorithm($selected_val, $input) {
            $obj1 = new Output();
            $filename = $input;
            $obj2 = new algorithms();
            $obj1->setOutput($filename,  $obj2->hashingAlgo($input, $selected_val),$selected_val);
        }
        
    }
    
    interface algos{
        function hashingAlgo($pass, $selected_val);
    }
    
    class algorithms implements algos {
        
        function hashingAlgo($pass, $selected_val) {
            try {
                $hash = hash($selected_val, $pass);
            } catch(Exception $e){
                echo "shite: " + $e;
            } finally {
                return $hash;
            }
        }
        
    }
    
    class Output {
    
        function setOutput($filename, $hash, $selected_val) {
            echo '
            <div style="display:inline-block; width: 400px;">
                <fieldset>
                    <legend>Output</legend>
                    <p style="color: white; background-color: black; text-align: left; height: auto; padding: 10px; word-break: break-all; word-wrap: break-word;">
                        User Input: '.$filename.'<br>
                        Algorithm: ' .$selected_val.'<br>
                        Generated Hash: '.$hash.'
                    </p> 
                </fieldset>
            </div>';
            unset($obj1);
            unset($obj2);
        }
        
    }
    
    $obj1 = new generateHash();
    $obj1->selectAlgorithm($selected_val, $input);    

}

    require_once 'footer.php';
?>
