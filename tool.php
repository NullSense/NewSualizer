<!DOCTYPE html>
<html lang="en">


<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
<link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.indigo-purple.min.css">
<script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>


<head>
    <meta charset="UTF-8">
    <title>HD TREE</title>
</head>

<div class="mdl-layout mdl-js-layout mdl-layout--fixed-header">
    <header class="mdl-layout__header">
        <div class="mdl-layout__header-row">
            <!-- Title -->
            <span class="mdl-layout-title">Dataset Dashboard</span>
            <!-- Add spacer, to align navigation to the right -->
            <div class="mdl-layout-spacer"></div>
            <!-- Navigation. We hide it in small screens. -->
            <nav class="mdl-navigation mdl-layout--large-screen-only">
                <a class="mdl-navigation__link" href="index.html">Landing Page</a>
                <a class="mdl-navigation__link" href="http://www.treevis.net">Treevis.net</a>
            </nav>
        </div>
    </header>
    <div class="mdl-layout__drawer">
        <span class="mdl-layout-title">Dataset Dahsboard</span>
        <nav class="mdl-navigation">
                <a class="mdl-navigation__link" href="index.html">Landing Page</a>
                <a class="mdl-navigation__link" href="http://www.treevis.net">Treevis.net</a>

        </nav>
    </div>
    <main class="mdl-layout__content">
        <div class="page-content">
            <!-- Your content goes here -->

            <style>
                .demo-card-wide.mdl-card {
                    width: 50%;
                    margin-top: 1%;
                    margin-left: 25%;
                }

                .demo-card-wide > .mdl-card__title {
                    color: #fff;
                    height: 176px;
                    background: url('https://images.pexels.com/photos/900108/pexels-photo-900108.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260') center / cover;
                }

                .demo-card-wide > .mdl-card__menu {
                    color: #fff;
                }
            </style>

            <div style="margin-left:25%; margin-top:2%;">
                <h2 style="color:blue" class="mdl-card__title-text">Step 1: Upload</h2>
            </div>

            <div class="demo-card-wide mdl-card mdl-shadow--2dp">
                <div class="mdl-card__title">
                </div>
                <div class="mdl-card__supporting-text">
                    Dataset format required : .tre, .txt
                </div>
                <div class="mdl-card__actions mdl-card--border">
                    <button onclick=showDiv(); class="mdl-button mdl-js-button mdl-button--raised mdl-button--colored">
                        Upload
                    </button>

                    <div id="wDiv" style="display:none;">
                        </br>
                        <form action="upload.php" method="post" enctype="multipart/form-data">
                            <input type="file" name="fileToUpload" id="fileToUpload">
                            <input type="submit" value="Upload Dataset" name="submit">
                        </form>
                    </div>
                </div>
                <div class="mdl-card__menu">
                    <button class="mdl-button mdl-button--icon mdl-js-button mdl-js-ripple-effect">
                        <i class="material-icons">share</i>
                    </button>
                </div>
            </div>


            <div style="margin-left: 25%; margin-top:2%;">
                <h2 style="color:blue" class="mdl-card__title-text">Step 2: Select dataset</h2>
            </div>
            <form action="vis.php" method="post">
                <table style="margin-left: 25%; margin-top:2%; width:50%;"
                       class="mdl-data-table mdl-js-data-table">
                    <thead>
                    <tr>
                        <th class="mdl-data-table__cell">Index</th>
                        <th class="mdl-data-table__cell--non-numeric">Dataset</th>
                        <th class="mdl-data-table__cell--non-numeric">Size(KB)</th>
                        <th class="mdl-data-table__cell">Upload Date</th>
                        <th class="mdl-data-table__cell">Checked</th>
                    </tr>
                    </thead>
                    <tbody>

                    <?php

                    $entries = scandir("HTML");
                    $filelist = array();
                    foreach ($entries as $entry) {

                        $entry = trim($entry, ".html");
                        $filelist[] = $entry;
                    }

                    $count = 0;
                    for ($i = 2; $i < count($filelist); $i++) {
                        $count++;
                        echo '<tr>';
                        echo '<td class="mdl-data-table__cell--">' . $count . '</td>';
                        echo '<td class="mdl-data-table__cell--non-numeric">' . $filelist[$i] . '</td>';
                        $str = 'HTML/' . $filelist[$i];
                        echo '<td class="mdl-data-table__cell">' . filesize($str) / 1000 . '</td>';
                        echo '<td class="mdl-data-table__cell">' . date("F d Y H:i:s.", filemtime($str)) . '</td>';
                        echo '<td><label><input type="checkbox" name= "dataset[]" id="dataset"  value="'.$filelist[$i].'"> </label> </td>';
                        echo '</tr>';

                    }


                    ?>


                    </tbody>
                </table>
                <input type="submit" value="submit" style="margin-left:25%; margin-top:2%;" class="mdl-button mdl-js-button mdl-button--raised mdl-button--colored" SHOW>
            </form>


        </div>
    </main>
</div>


<body>


<script>

    var table = document.querySelector('table');
    var headerCheckbox = table.querySelector('thead .mdl-data-table__select input');
    var boxes = table.querySelectorAll('tbody .mdl-data-table__select');
    var headerCheckHandler = function (event) {
        if (event.target.checked) {
            for (var i = 0, length = boxes.length; i < length; i++) {
                boxes[i].MaterialCheckbox.check();
                boxes[i].MaterialCheckbox.updateClasses();
            }
        } else {
            for (var i = 0, length = boxes.length; i < length; i++) {
                boxes[i].MaterialCheckbox.uncheck();
                boxes[i].MaterialCheckbox.updateClasses();
            }
        }
    };
    headerCheckbox.addEventListener('change', headerCheckHandler);


    function showDiv() {
        document.getElementById('wDiv').style.display = "block";
    }
</script>
</body>
</html>