import django.db.models
import django.utils.safestring
import course.validators
import colorfield.fields
import django.contrib.auth.models


class Tag(django.db.models.Model):
    name = django.db.models.CharField(
        verbose_name='Название',
        max_length=50,
        unique=True,
    )
    background_color = colorfield.fields.ColorField(
        verbose_name='Цвет фона',
        default='#E94F37',
    )
    
    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'
    
    def __str__(self) -> str:
        return self.name
    
    def render_tag(self) -> str:
        return django.utils.safestring.mark_safe(
            f'<span style="background-color: {self.background_color}; padding: 0.35em 0.65em;'
            'font-size: 1em; font-weight: 700; line-height: 1.5; color: #fff; text-align: center;'
            f'white-space: nowrap; vertical-align: baseline; border-radius: 50rem;">{self.name}</span>'
        )
    
    render_tag.short_description = 'тег'
    render_tag.allow_tags = True

    def render_tag_outline(self) -> str:
        return django.utils.safestring.mark_safe(
            f'<span style="padding: 0.35em 0.65em; background-color: #212529'
            'font-size: 1em; font-weight: 700; line-height: 1.5; color: #fff; text-align: center;'
            'white-space: nowrap; vertical-align: baseline; border-radius: 50rem;'
            f'border: 2px solid {self.background_color};">{self.name}</span>'
        )
    
    render_tag_outline.short_description = 'контур'
    render_tag_outline.allow_tags = True


class Course(django.db.models.Model):
    title = django.db.models.CharField(
        verbose_name='Название', 
        max_length=150,
        unique=True,
    )
    lead = django.db.models.TextField(
        verbose_name='Лид', 
        max_length=250,
    )
    introduction = django.db.models.TextField(
        verbose_name='Вступление',
    )
    tags = django.db.models.ManyToManyField(
        verbose_name='Теги',
        to=Tag,
    )
    is_published = django.db.models.BooleanField(
        verbose_name='Опубликовано',
        default=True,
    )
    private = django.db.models.BooleanField(
        verbose_name='Сделать курс приватным',
        default=False,
    )
    access = django.db.models.ManyToManyField(
        verbose_name='Пользователи с доступом к курсу',
        to=django.contrib.auth.models.User,
    )
    
    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курс'
    
    def __str__(self) -> str:
        return self.title


class Lesson(django.db.models.Model):
    title = django.db.models.CharField(
        verbose_name='Название', 
        max_length=150,
    )
    theory = django.db.models.TextField(
        verbose_name='Теория',
    )
    course = django.db.models.ForeignKey(
        verbose_name='Курс',
        to=Course,
        on_delete=django.db.models.CASCADE,
        null=True,
        blank=True,
    )
    is_published = django.db.models.BooleanField(
        verbose_name='Опубликовано',
        default=True,
    )
    
    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
    
    def __str__(self) -> str:
        return self.title


class Task(django.db.models.Model):
    title = django.db.models.CharField(
        verbose_name='Название', 
        max_length=150,
    )
    difficulty = django.db.models.IntegerField(
        verbose_name='Сложность',
        choices=(
            (1, '*'),
            (2, '**'),
            (3, '***'),
        ),
        default=1,
    )
    time_limit = django.db.models.IntegerField(
        verbose_name='Ограничение времени',
        default=1,
        validators=[course.validators.validate_more_zero],
        help_text='(секунд)',
    )
    memory_limit = django.db.models.IntegerField(
        verbose_name='Ограничение памяти',
        default=64,
        validators=[course.validators.validate_more_zero],
        help_text='(Mb)',
    )
    input_type = django.db.models.CharField(
        verbose_name='Ввод',
        max_length=100,
        default='стандартный ввод или input.txt',
    )
    output_type = django.db.models.CharField(
        verbose_name='Вывод',
        max_length=100,
        default='стандартный вывод или output.txt',
    )
    text = django.db.models.TextField(
        verbose_name='Текст задания',
    )
    input_format = django.db.models.TextField(
        verbose_name='Формат ввода',
        blank=True,
    )
    output_format = django.db.models.TextField(
        verbose_name='Формат вывода',
        blank=True,
    )
    lesson = django.db.models.ForeignKey(
        verbose_name='Урок',
        to=Lesson,
        on_delete=django.db.models.CASCADE,
        null=True,
        blank=True,
    )
    is_published = django.db.models.BooleanField(
        verbose_name='Опубликовано',
        default=True,
    )
    solution = django.db.models.TextField(
        verbose_name='Решение автора',
        default='<pre class="language-python">&nbsp;</pre>',
        blank=True,
    )

    class Meta:
        verbose_name = 'задание'
        verbose_name_plural = 'задания'
    
    def __str__(self) -> str:
        return self.title
    
    def get_time_limit(self) -> str:
        if 11 <= self.time_limit <= 19 or 5 <= self.time_limit % 10 <= 9 or self.time_limit % 10 == 0:
            return f'{self.time_limit} секунд'
        elif self.time_limit % 10 == 1:
            return f'{self.time_limit} секунда'
        elif 2 <= self.time_limit % 10 <= 4:
            return f'{self.time_limit} секунды'

    get_time_limit.allow_tags = True
    get_time_limit.short_description = 'Время'

    def get_memory_limit(self) -> str:
        return f'{self.memory_limit}Mb'
    
    get_memory_limit.allow_tags = True
    get_memory_limit.short_description = 'Память'
    

class Example(django.db.models.Model):
    input_data = django.db.models.TextField(
        verbose_name='Ввод',
        blank=True,
        null=True,
    )
    output_data = django.db.models.TextField(
        verbose_name='Вывод',
        blank=True,
        null=True,
    )
    task = django.db.models.ForeignKey(
        verbose_name='Задание',
        to=Task,
        on_delete=django.db.models.CASCADE,
        null=True,
        blank=True,
    )
    is_published = django.db.models.BooleanField(
        verbose_name='Опубликовано',
        default=True,
    )
    
    class Meta:
        verbose_name = 'пример'
        verbose_name_plural = 'примеры'
    
    def __str__(self) -> str:
        return str(self.id)


class PrivateMaterial(django.db.models.Model):
    title = django.db.models.CharField(
        verbose_name='Название', 
        max_length=150,
    )
    text = django.db.models.TextField(
        verbose_name='Текст',
    )
    lead = django.db.models.TextField(
        verbose_name='Лид', 
        max_length=250,
        blank=True,
    )
    is_published = django.db.models.BooleanField(
        verbose_name='Опубликовано',
        default=True,
    )
    access = django.db.models.ManyToManyField(
        verbose_name='Пользователи с доступом к материалу',
        to=django.contrib.auth.models.User,
    )

    class Meta:
        verbose_name = 'приватный материал'
        verbose_name_plural = 'приватные материалы'
    
    def __str__(self) -> str:
        return self.title
