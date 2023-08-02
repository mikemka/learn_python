var app = new Vue({
    el: '#app',
    data: {
        defaultGroup: '',
        buttonBar: [],
        buttonGroups: {},
        currentGroup: [],
        mathField: '',
        latex: '',
        mathLiveConfig: {},
    },
    created() {
        if (window.addEventListener) {
            // For standards-compliant web browsers
            window.addEventListener('message', this.getParams, false);
        } else {
            window.attachEvent('onmessage', this.getParams);
        }
    },

    mounted() {
        setTimeout(function() {
            MathLive.renderMathInDocument();
        }, 200);
        window.parent.postMessage(
            {
                mceAction: 'equation-mounted',
                status: true,
            },
            '*'
        );
    },

    methods: {
        collapse(event) {
            event.target.classList.toggle('active');
            var content = event.target.nextElementSibling;
            if (content.style.maxHeight) {
                content.style.maxHeight = null;
            } else {
                content.style.maxHeight = content.scrollHeight + 'px';
            }
        },
        getParams(evt) {
            let data = evt.data;
            /*
            console.log('received', data);
            */
            this.defaultGroup = data.equation_editor_group;
            this.buttonBar = data.equation_editor_button_bar;
            this.buttonGroups = data.equation_editor_button_groups;
            this.currentGroup = this.buttonGroups[this.defaultGroup];
            this.latex = data.latex;
            this.mathLiveConfig = data.mathlive_config;
            this.initEquation();
            this.mathField.focus();
        },

        initEquation() {
            this.mathField = new MathfieldElement();
            
            this.mathField.addEventListener('input', (ev) => {
                this.latex = this.mathField.getValue();
                this.sendLatex();
            });

            if (typeof this.mathLiveConfig === 'object') {
                if (Object.keys(this.mathLiveConfig).length) {
                    this.mathField.setOptions(this.mathLiveConfig);
                }
            }

            if (this.latex) {
                this.mathField.setValue(this.latex);
            }

            document.getElementById('math-field').appendChild(this.mathField);
        },

        insert(button) {
            this.mathField.insert(button.latex, {
                focus: true,
            });
        },

        sendLatex() {
            var content = {
                mceAction: 'equation-update',
                html: MathLive.convertLatexToMarkup(this.latex),
                latex: this.latex,
            }
            //console.info('Send', content);
            window.parent.postMessage(content, '*');
        },
    },
});
