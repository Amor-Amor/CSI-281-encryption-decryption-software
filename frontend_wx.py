# Author: Harrison Hennessy
#
# Lock Image from:
# https://www.clipartmax.com/middle/m2i8A0Z5b1K9Z5G6_lock-key-private-safe-password-secure-comments-encryption-icon-png/


# Import wxPython library
import wx
import csi280_codec
import os

# creates cyphers to be used for encoding/decoding
subst_cypher = csi280_codec.SubstitutionCypher.new_cypher()
rot13_cypher = csi280_codec.SubstitutionCypher.Rot13()

# Frame Class


class Encryption_Frame(wx.Frame):

    # Sets up GUI on initialization
    def __init__(self, *args, **kw):
        super(Encryption_Frame, self).__init__(*args, **kw)

        # Creates main GUI panel and vertical sizer
        main_panel = wx.Panel(self)
        main_panel.SetBackgroundColour(wx.Colour(0, 0, 0))
        vbox = wx.BoxSizer(wx.VERTICAL)
        main_panel.SetSizer(vbox)

        # Specifies main GUI font
        font = wx.Font(15, wx.FONTFAMILY_ROMAN,
                       wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

        # Specifies header font
        header_font = wx.Font(24, wx.FONTFAMILY_TELETYPE,
                              wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        # Logo Image
        filepath = os.getcwd() + '\\assets\logo.png'
        image = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
        bitmap = wx.StaticBitmap(main_panel, -1, wx.BitmapFromImage(image))
        vbox.Add(bitmap, 1, wx.ALIGN_CENTER_HORIZONTAL, 0)

        # Sets up horizontal sizer for second row
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        vbox.Add(hbox1, 1, wx.ALIGN_CENTER_HORIZONTAL, 30)

        # Label for algorithm selector
        select_algorithm_label = wx.StaticText(
            main_panel, label="Select Algorithm: ")
        select_algorithm_label.SetFont(font)
        select_algorithm_label.SetForegroundColour(wx.Colour(255, 255, 255))
        hbox1.Add(select_algorithm_label, 1, wx.ALIGN_CENTER_VERTICAL, 30)

        # Algorithm selector
        algorithms = ['Substitution',
                      'Permutation (WIP)', 'Caesar', 'Rot13', 'None']
        self.algorithm_selector = wx.ComboBox(
            main_panel, value="None", choices=algorithms, style=wx.CB_READONLY)
        self.algorithm_selector.SetFont(font)
        self.algorithm_selector.SetForegroundColour(wx.Colour(255, 255, 255))
        self.algorithm_selector.SetBackgroundColour(wx.Colour(0, 0, 0))
        hbox1.Add(self.algorithm_selector, 1, wx.ALIGN_CENTER_VERTICAL, 30)

        # Sets up horizontal spacer for third row
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        vbox.Add(hbox2, 1, wx.ALIGN_CENTER_HORIZONTAL, 30)

        # Text entry label
        text_entry_label = wx.StaticText(main_panel, label="Enter Text:")
        text_entry_label.SetFont(font)
        text_entry_label.SetForegroundColour(wx.Colour(255, 255, 255))
        hbox2.Add(text_entry_label, 1, wx.ALIGN_CENTER_VERTICAL, 30)

        # Text entry box
        self.text_entry = wx.TextCtrl(main_panel, -1, "", size=(150, 25))
        self.text_entry.SetFont(font)
        self.text_entry.SetForegroundColour(wx.Colour(255, 255, 255))
        self.text_entry.SetBackgroundColour(wx.Colour(0, 0, 0))
        hbox2.Add(self.text_entry, 1, wx.ALIGN_CENTER_VERTICAL, 30)

        # Buffer space
        hbox2.Add((1, 1), 1)

        # Key entry label
        key_entry_label = wx.StaticText(main_panel, label="Enter Key:")
        key_entry_label.SetFont(font)
        key_entry_label.SetForegroundColour(wx.Colour(255, 255, 255))
        hbox2.Add(key_entry_label, 1, wx.ALIGN_CENTER_VERTICAL, 30)

        # Key entry box
        self.key_entry = wx.TextCtrl(main_panel, -1, "", size=(150, 25))
        self.key_entry.SetFont(font)
        self.key_entry.SetForegroundColour(wx.Colour(255, 255, 255))
        self.key_entry.SetBackgroundColour(wx.Colour(0, 0, 0))
        hbox2.Add(self.key_entry, 1, wx.ALIGN_CENTER_VERTICAL, 30)

        # Sets up horizontal spacer for fourth row
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        vbox.Add(hbox3, 1, wx.ALIGN_CENTER_HORIZONTAL, 30)

        # Encrypt button
        encrypt_button = wx.Button(main_panel, label="Encrypt")
        encrypt_button.SetFont(font)
        encrypt_button.SetForegroundColour(wx.Colour(255, 255, 255))
        encrypt_button.SetBackgroundColour(wx.Colour(0, 0, 0))
        encrypt_button.Bind(wx.EVT_BUTTON, self.click_encrypt_button_wx)
        hbox3.Add(encrypt_button, 1, wx.ALIGN_CENTER_VERTICAL, 100)

        # Buffer space
        hbox3.Add((1, 1), 1)

        # Decrypt button
        decrypt_button = wx.Button(main_panel, label="Decrypt")
        decrypt_button.SetFont(font)
        decrypt_button.SetForegroundColour(wx.Colour(255, 255, 255))
        decrypt_button.SetBackgroundColour(wx.Colour(0, 0, 0))
        decrypt_button.Bind(wx.EVT_BUTTON, self.click_decrypt_button_wx)
        hbox3.Add(decrypt_button, 1, wx.ALIGN_CENTER_VERTICAL, 100)

        # Sets up horizontal spacer for fifth row
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        vbox.Add(hbox4, 1, wx.ALIGN_CENTER_HORIZONTAL, 30)

        # Output label
        output_label = wx.StaticText(main_panel, label="Output:")
        output_label.SetFont(font)
        output_label.SetForegroundColour(wx.Colour(255, 255, 255))
        hbox4.Add(output_label, 1, wx.ALIGN_CENTER_VERTICAL)

        # Output box
        self.output_box = wx.TextCtrl(main_panel, -1, "", size=(300, 25))
        self.output_box.SetFont(font)
        self.output_box.SetForegroundColour(wx.Colour(255, 255, 255))
        self.output_box.SetBackgroundColour(wx.Colour(0, 0, 0))
        hbox4.Add(self.output_box, 1, wx.ALIGN_CENTER_VERTICAL)

    # Event handler for encrypt button

    def click_encrypt_button_wx(self, event):
        if self.algorithm_selector.GetStringSelection() == 'Substitution':
            encoded_text = subst_cypher.encode(self.text_entry.GetLineText(0))
            self.output_box.SetValue("")
            self.output_box.write(encoded_text)
        elif self.algorithm_selector.GetStringSelection() == 'Permutation':
            encoded_text = csi280_codec.PermutationCypher.encode(
                self.text_entry.GetLineText(0))
            self.output_box.SetValue("")
            self.output_box.write(encoded_text)
        elif self.algorithm_selector.GetStringSelection() == 'Caesar':
            caesar_cypher = csi280_codec.SubstitutionCypher.Caeser(
                int(self.key_entry.GetLineText(0)))
            encoded_text = caesar_cypher.encode(self.text_entry.GetLineText(0))
            self.output_box.SetValue("")
            self.output_box.write(encoded_text)
        elif self.algorithm_selector.GetStringSelection() == 'Rot13':
            encoded_text = rot13_cypher.encode(self.text_entry.GetLineText(0))
            self.output_box.SetValue("")
            self.output_box.write(encoded_text)
        elif self.algorithm_selector.GetStringSelection() == 'None':
            self.output_box.SetValue("")
            self.output_box.write(self.text_entry.GetLineText(0))

    # Event handler for decrypt button
    def click_decrypt_button_wx(self, event):
        if self.algorithm_selector.GetStringSelection() == 'Substitution':
            decoded_text = subst_cypher.decode(self.text_entry.GetLineText(0))
            self.output_box.SetValue("")
            self.output_box.write(decoded_text)
        elif self.algorithm_selector.GetStringSelection() == 'Permutation':
            decoded_text = csi280_codec.PermutationCypher.decode(
                self.text_entry.GetLineText(0))
            self.output_box.SetValue("")
            self.output_box.write(decoded_text)
        elif self.algorithm_selector.GetStringSelection() == 'Caesar':
            caesar_cypher = csi280_codec.SubstitutionCypher.Caeser(
                int(self.key_entry.GetLineText(0)))
            decoded_text = caesar_cypher.decode(self.text_entry.GetLineText(0))
            self.output_box.SetValue("")
            self.output_box.write(decoded_text)
        elif self.algorithm_selector.GetStringSelection() == 'Rot13':
            decoded_text = rot13_cypher.decode(self.text_entry.GetLineText(0))
            self.output_box.SetValue("")
            self.output_box.write(decoded_text)
        elif self.algorithm_selector.GetStringSelection() == 'None':
            self.output_box.SetValue("")
            self.output_box.write(self.text_entry.GetLineText(0))


# Creates and starts application Object
front_end = wx.App()
main_frame = Encryption_Frame(
    None, title="Encryption/Decryption GUI 2", size=(800, 400))
main_frame.Show()

# Starts main loop
front_end.MainLoop()
