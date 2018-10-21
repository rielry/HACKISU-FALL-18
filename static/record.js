$(document).ready(function () {

    var record = document.querySelector('#recordButton');
    var stop = document.querySelector('#stopButton');
    var soundClips = document.querySelector('.sound-clips');

    record.onclick = function () {
        if (navigator.mediaDevices) {
            console.log('getUserMedia supported.');

            var constraints = { audio: true };
            var chunks = [];

            navigator.mediaDevices.getUserMedia(constraints)
                .then(function (stream) {

                    var mediaRecorder = new MediaRecorder(stream);

                    mediaRecorder.start();
                    console.log(mediaRecorder.state);
                    console.log("recorder started");
                    record.style.background = "red";
                    record.style.color = "black";

                    stop.onclick = function () {
                        mediaRecorder.stop();
                        console.log(mediaRecorder.state);
                        console.log("recorder stopped");
                        record.style.background = "";
                        record.style.color = "";
                    }

                    mediaRecorder.onstop = function (e) {
                        console.log("data available after MediaRecorder.stop() called.");

                        var clipName = 'recording';

                        var clipContainer = document.createElement('article');
                        var clipLabel = document.createElement('p');
                        var audio = document.createElement('audio');
                        var deleteButton = document.createElement('button');
                        deleteButton.className = 'btn btn-light btn-lg lead cover';

                        clipContainer.classList.add('clip');
                        audio.setAttribute('controls', '');
                        deleteButton.innerHTML = "Delete";
                        clipLabel.innerHTML = clipName;

                        clipContainer.appendChild(audio);
                        clipContainer.appendChild(deleteButton);
                        soundClips.appendChild(clipContainer);

                        audio.controls = true;
                        var blob = new Blob(chunks, { 'type': 'audio/wav; codecs=opus' });
                        chunks = [];
                        var audioURL = URL.createObjectURL(blob);
                        audio.src = audioURL;
                        console.log("recorder stopped");

                        var formData = new FormData();
                        formData.append('audio', blob, 'recording.wav');

                        $.ajax({
                            type: 'POST',
                            url: '/getblob',
                            data: formData,
                            dataType: 'json',
                            processData: false,
                            contentType: false
                        });

                        stream.getTracks().forEach(track => track.stop());

                        deleteButton.onclick = function (e) {
                            evtTgt = e.target;
                            evtTgt.parentNode.parentNode.removeChild(evtTgt.parentNode);
                        }
                    }

                    mediaRecorder.ondataavailable = function (e) {
                        chunks.push(e.data);
                    }
                })
                .catch(function (err) {
                    console.log('The following error occurred: ' + err);
                })
        }
    }

});